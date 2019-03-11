# text-to-image-with-SNGAN-and-WGAN
TEXT TO IMAGE GANs inclufing tons of GANs models AND LOTS OF TRIALS with spaghetti code


관련 논문 목록 https://github.com/wooramkang/Papers-for-image-caption-and-text-to-image.git



# 세상 불친절한 git repo

코드를 돌리기 위한 준비물

1. glove 임베딩 100dim, 200dim, 300dim 각각에 pretrained 파일 (검색하면 나온다)
2. caption 과 image 쌍으로 이루어진 데이터셋 (검색하면 다양한 데이터 셋이 많이 나온다. 해보고 싶은 것을 찾는다)
3. 충분한 컴퓨팅파워가 보장된 환경


코드 돌려보기
1. 학습하고자 할때 dcgan_train.py 실행
2. 학습된 결과를 중간에 생성해보고자 할때 dcgan_generate.py 실행
3. 다만 스파게티가 매우 꼬여 있어서 TXT2IMAGE/library/dcgan_v3.py안쪽을 정리하며 목적에 맞게 수정후 주석을 풀고 실행
4. 다른 형태로 트라이얼 하고자 할때는 각각의 다른 코드뭉치를 주석을 풀고 실행
