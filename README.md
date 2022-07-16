# Overview / 概要
卒業研究で機械学習･深層学習を用いたオンライン試験のカンニング検出システムを作成する予定｡

## 今後の課題
大まかに予想されるオンライン試験のカンニングのシチュエーション

1.パソコンの傍ににスマホや紙といった資料を置いてカンニングをしている

->以下のような顔の傾きの特徴量から大まかに検出できると予想

![face240png](https://user-images.githubusercontent.com/61785070/178117466-bb42f027-c22d-4fe2-9cbb-eb365b8538a9.png)

![face280png](https://user-images.githubusercontent.com/61785070/178117468-a9eb45de-6323-4b2f-a1bd-badb06909e9f.png)

![face440png](https://user-images.githubusercontent.com/61785070/178117473-99f4d03b-733a-4744-853e-6d898f1d35c8.png)

2.第三者との会話でカンニングをしている｡

->口元の開き具合から会話をしているか検出できると予想できる｡

3.パソコンの画面上で資料となるファイルを開きながら受験している｡もしくは､パソコンの画面にメモを貼り付けながら受験している｡

->右目か左目の黒目の位置からどちらを向いているか検出するようにする｡(現在､取り組み中)



->書き出したcsvファイルに対してlightgbm/tensorflow/scikit-learn等を使ってモデルを作成して検出モデルを作成する予定｡

->最終的に作成した精度､フレームレートの高さを検出モデルで比較を行なう｡

# Installation / 使用方法
```bash
pip install opencv-python
```
```bash
pip install pandas
```
```bash
pip install face-utils
```
```bash
pip install dlib
```
```bash
pip install opencv-python
```
