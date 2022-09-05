# opyrator launch-ui main:generate_text
import torch
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel

tokenizer = PreTrainedTokenizerFast.from_pretrained(
    "skt/kogpt2-base-v2",
    bos_token='</s>',
    eos_token='</s>',
    unk_token='<unk>',
    pad_token='<pad>',
    mask_token='<mask>')

model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')
text = '인생을 즐겁게 살기 위해서는'
input_ids = tokenizer.encode(text, return_tensors='pt')
gen_ids = model.generate(input_ids,
                         max_length=128,
                         repetition_penalty=2.0,
                         pad_token_id=tokenizer.pad_token_id,
                         eos_token_id=tokenizer.eos_token_id,
                         bos_token_id=tokenizer.bos_token_id,
                         use_cache=True)
generated = tokenizer.decode(gen_ids[0])
print(generated)

'''
<OUTPUT 결과 값>
인생을 즐겁게 살기 위해서는 무엇보다 자신의 능력을 최대한 발휘해야 한다.
그렇지 않으면 성공할 수 없다.
성공하는 사람은 자신이 가진 재능을 마음껏 발휘할 줄 아는 사람이다.
자신의 재능과 열정, 그리고 열정을 바탕으로 한 자기계발서가 필요하다.
자기 계발서 1
1. 자신을 위한 준비와 계획 수립하기
2. 자신에게 맞는 학습 방법을 찾아라!
3. 스스로 공부하는 습관을 길러라.
4. 자신만의 공부법을 만들어 보라.
5. 자신감을 갖고 꾸준히 노력하라!
'''
