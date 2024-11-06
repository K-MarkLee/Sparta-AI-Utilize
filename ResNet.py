from fastai.vision.all import *
import matplotlib.pyplot as plt
import numpy

print(numpy.version.version)  # Print NumPy version
# 데이터셋 로드
path = untar_data(URLs.PETS)  # PETS 데이터셋 다운로드 및 압축 해제
path_imgs = path/'images'
# 이미지 파일 라벨링 함수 정의
def is_cat(x): return x[0].isupper()


if torch.cuda.is_available():
    print("GPU is available. Running on GPU.")
    device = 'cuda' 
else:
    print("GPU is not available. Running on CPU.")
    device = 'cpu'

if __name__ == '__main__':
    # 데이터블록 정의
    dls = ImageDataLoaders.from_name_func(
        path_imgs, get_image_files(path_imgs), valid_pct=0.2, seed=42,
        label_func=is_cat, item_tfms=Resize(224)
    )
    # 데이터셋 확인
    dls.show_batch(max_n=9, figsize=(7, 6))
    # ResNet34 사전 학습된 모델을 사용해 학습기 생성
    learn = cnn_learner(dls, resnet34, metrics=error_rate)
    # 학습률 찾기 (최적의 학습률을 자동으로 찾아줌)
    learn.lr_find()
    # 모델 학습 (사전 학습된 모델에 대해 파인 튜닝)
    learn.fine_tune(3)
    # 모델 평가
    learn.show_results()
    # 혼동 행렬 (Confusion Matrix) 출력
    interp = ClassificationInterpretation.from_learner(learn)
    interp.plot_confusion_matrix()
    # 새로운 이미지에 대한 예측
    img = PILImage.create('path_to_yourimage.jpg')
    pred, _, probs = learn.predict(img)
    # 결과 출력
    print(f"Prediction: {pred}, Probability: {probs.max():.4f}")
    img.show()
