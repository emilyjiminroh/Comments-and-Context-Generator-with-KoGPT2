# Comments and Context Generator with KoGPT2 model

## [My Blog](https://rotoma-code.tistory.com/entry/KoGPT-2-%EB%AC%B4%ED%95%9C%EB%8F%84%EC%A0%84-%EC%BB%A8%ED%85%90%EC%B8%A0-%EB%A7%9E%EC%B6%A4%ED%98%95-%EB%8C%93%EA%B8%80-%EC%9E%90%EC%9C%A0-%EC%A3%BC%EC%A0%9C-%EB%AC%B8%EC%9E%A5-%EC%83%9D%EC%84%B1%EA%B8%B0)


### KoGPT2 SKT-AI Github
https://github.com/SKT-AI/KoGPT2

### Until the Project Topic Set
이번 프로젝트의 주제를 선정하기 앞써 실무 교육에서 들었던 여러가지 AI 알고리즘 중 NLP, 자연어 처리 알고리즘에 흥미를 느꼈다. 평소 CV 컴퓨터 비젼이나 영상 처리, 3D 분야에 관심이 있어, 직접적으로 NLP를 다뤄보지 못했었는데, 이번 실무 교육에서 Transformer architecture, Attention, GPT, BERT 등 논문 리뷰를 통해 보다 논리적으로, 수학적으로 접근하면서 이해할 수 있어서 더욱 신기하면서, 흥미를 가질 수 있게 되었다. 그래서 이번 기회에 NLP를 활용하여 프로젝트를 진행해보면 재미겠다는 마음으로 우선 도전했다. 주제를 선정하고 아래와 같이 사용하고자 했던 GPT 모델을 먼저 확실하게 이해하고자 했다. 


### Goal of this project
프로젝트를 구상하기 앞써, 현재 내가 활용할 수 있는 툴에 어떤 것이 있는지 점검해보았다. 그리고 활용하고자 하는 구체적인 목표를 세워 프로젝트를 구상했다. 실무교육에서 다뤘던 GCP, Anaconda 를 활용한 프로젝트를 목표로 잡고 매진했다.

![005](https://user-images.githubusercontent.com/71576768/188349735-0122443b-0c03-4e30-9833-c2c45519c820.jpg)

### About GPT model (difference with Transformer Architecture)
![007](https://user-images.githubusercontent.com/71576768/188349800-d052efd4-13e4-4a66-ac60-f5bc257b8e01.jpg)

### Comments Generator with Colab
앞써 발견한 reference를 그대로 따라 프로젝트를 진행한다면 너무 개성도 없고, 재미도 덜하는 기계적인 프로젝트 개발이 될 것 같아, 첫 번째 프로젝트로, SKT에서 개발한 KoGPT 모델을 나만의 모델로 Fine-Tuning 해서 댓글 생성기 프로젝트를  진행했다. 이때 Fine-Tuning 할 데이터 셋은 GCP의 Youtube Data API를 사용해 평소 즐겨 보던, 무한도전 유튜브 채널의 댓글을 크롤링하여, 무한도전 컨텐츠 맞춤형 댓글 생성기를 제작했다. 자세한 구현 과정은 아래와 같다.

![009](https://user-images.githubusercontent.com/71576768/188349899-8243b468-0f8a-4cf6-9a35-1729009be214.jpg)

### Context Generator with Opyrator
두 번째로는 본격 Anaconda 활용 제대로된 문장 생성기를 만들어 봐야겠다는 마음으로 단순하지만, 고도의 신기한, 말이 진짜 되는 문장 생성기 프로젝트를 진행했다. 이번에는 Opyrator을 사용하여, 제대로된 UI를 가지고 테스트 까지 해볼 수 있는 프로젝트이다.

![011](https://user-images.githubusercontent.com/71576768/188349902-0c57fa30-de2f-434a-8ca0-e5676bb0395b.jpg)

### At Last ,
혼자 처음으로 진행했던 AI 프로젝트인 만큼 상당 시간을 외부 reference를 찾는 시간으로 가득했던 것 같다. 처음에는 뭘 해야할지 막막하다는 생각에 프로젝트 구상 아이디어도 많이 떠오르지 않았지만, 확실히 처음부터 여러가지를 구글링 하면서, 직접 뭐라도 찾아 Trouble Shooting을 해 가며, 일단 저질러 보는 것이 이번 프로젝트에 매우 많은 도움이 되었다. 이번에 실무교육을 통해 Paper Review의 재미를 알게 된 만큼 여러 논문을 리뷰 하는 것에 도전해보고 싶다. 또, 논문을 읽고 이렇게 간단하지만 알찬 프로젝트를 통해 여러 인공지능 모델을 좀 더 잘 이해하고 싶다. 
