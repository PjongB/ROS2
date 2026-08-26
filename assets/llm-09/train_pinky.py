from unsloth import FastLanguageModel
import torch
from datasets import Dataset
import json
from trl import SFTTrainer
from transformers import TrainingArguments

# 1. Configuration
max_seq_length = 2048
dtype = None # Auto detection
load_in_4bit = True
input_json = "pinky_finetune_data.json"
model_name = "unsloth/Qwen3-4B-unsloth-bnb-4bit" # Using the one from the notebook

# 2. Load Model
print("Loading Model...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_name,
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# 3. Add LoRA Adapters
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Adjust rank if needed (16, 32, 64)
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
    use_rslora = False,
    loftq_config = None,
)

# 4. Prepare Dataset
print("Preparing Dataset...")
with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# 시스템 프롬프트 정의
system_prompt = """당신은 교육용 로봇 'Pinky'를 제어하는 Python 전문가입니다.
사용자의 요청에 대해 `pinkylib`과 `pinky_lcd` 라이브러리를 사용하여 정확한 Python 코드를 작성하세요.
반드시 제공된 Pinky 라이브러리 명세에 정의된 클래스와 함수만 사용하세요.
하드웨어 제어 코드는 try-finally로 작성하고, 장치 명세에 정의된 close(), clean(), clear() 등의 종료 메서드로 안전하게 정리하세요.
모르는 내용이거나 라이브러리에 없는 기능이라면 억지로 코드를 만들지 말고 솔직하게 "모르겠습니다"라고 대답하세요.
답변은 한국어로 친절하게 설명하세요."""

def format_prompt(example):
    input_text = example['input']
    output_text = example['output']

    # 시스템 프롬프트
    system_message = system_prompt

    # [표준 Alpaca 포맷 적용]
    text = f"""### Instruction:
{system_message}

{input_text}

### Response:
{output_text}"""

    return text + tokenizer.eos_token

# Convert to HuggingFace Dataset
formatted_data = [{"text": format_prompt(item)} for item in data]
dataset = Dataset.from_list(formatted_data)

# 5. Train
print("Starting Training...")
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    args = TrainingArguments(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 10,
        num_train_epochs = 10,
        learning_rate = 2e-4,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "pinky_outputs",
    ),
)

trainer_stats = trainer.train()

# 6. Save Model
print("Saving Model...")
# model.save_pretrained("pinky_lora_model")
# tokenizer.save_pretrained("pinky_lora_model")

# Merge to GGUF
model.save_pretrained_gguf("pinky_model", tokenizer, quantization_method = "q4_k_m")
print("Done!")
