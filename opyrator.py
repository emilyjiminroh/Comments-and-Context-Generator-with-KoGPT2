# opyrator launch-ui main:generate_text
import torch
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel
from pydantic import BaseModel, Field  # opyrator

tokenizer = PreTrainedTokenizerFast.from_pretrained(
    "skt/kogpt2-base-v2",
    bos_token='</s>',
    eos_token='</s>',
    unk_token='<unk>',
    pad_token='<pad>',
    mask_token='<mask>')

model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')


class Input(BaseModel):
    text: str = Field(
        title='문장을 입력해주세요',
        max_length=128
    )
    max_length: int = Field(
        128,
        ge=5,  # greater than equal 크거나 같다
        le=128  # less than equal 작거나 같다
    )
    repetition_penalty: float = Field(  # 반복 패널티
        2.0,
        ge=0.0,
        le=2.0
    )


class Output(BaseModel):
    generated_text: str


def generate_text(input: Input) -> Output:
    input_ids = tokenizer.encode(input.text)
    gen_ids = model.generate(torch.tensor([input_ids]),
                             max_length=input.max_length,
                             repetition_penalty=input.repetition_penalty,
                             pad_token_id=tokenizer.pad_token_id,
                             eos_token_id=tokenizer.eos_token_id,
                             bos_token_id=tokenizer.bos_token_id,
                             use_cache=True)

    generated = tokenizer.decode(gen_ids[0, :].tolist())
    return Output(generated_text=generated)
