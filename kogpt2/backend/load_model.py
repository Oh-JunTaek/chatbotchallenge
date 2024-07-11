from transformers import GPT2LMHeadModel, GPT2TokenizerFast

def load_kogpt2():
    model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")
    tokenizer = GPT2TokenizerFast.from_pretrained("skt/kogpt2-base-v2")
    return model, tokenizer

if __name__ == "__main__":
    model, tokenizer = load_kogpt2()
    print("KoGPT-2 모델과 토크나이저가 성공적으로 로드되었습니다.")
