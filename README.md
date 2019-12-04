# DIVE INTO CODE 卒業課題
## 7月期生　森　修弥
### 簡易的医療画像分類モデル作成<br>
---------------------------------------------------------------------------------------------------<br>
・やったこと：google検索で取得した手の病気の画像を分類するモデルを作成した。<br>
・理由：医療業界の問題解決のため、一般人が自分で使える簡単な診断システムを作ってみたかった。<br>
・プロジェクトの要点:医療分野ならではの問題を考慮に入れた評価指標を作成し、それに伴う損失関数やモデルを作成した。<br>
・方法：様々なモデルを作成し、結果を比べた。詳細はHistory.ipynbに記載<br>
・結果：正解率ならVGG19-categorical_crossentropy, 軽症だと誤判定する割合の低さなら,VGG16+SVM-custom_loss。<br>
     詳細はHistory.ipynbに記載。<br>

![result](https://user-images.githubusercontent.com/50583880/67921415-f69e4f80-fbea-11e9-8c56-d05e5860553d.png)
・学んだこと：タスクによって損失関数や評価指標選ばなければならないことを学んだ。<br>
<br>
Introduce.pdfにスライドとしてプロジェクトの概要を記載。<br>
このプロジェクトにおいて行ったことのまとめはNotebook"History"に記載する。<br>

ベイズ推定をしてみた。notebook(bays.ipynb)に記載している。<br>
別の推定方法を試してみた。notebook(AutoEncoder-KMeans.ipynb)に記載<br>
---------------------------------------------------------------------------------------------------<br>
GUIクイックスタート<br>
cd GUI<br>
python self_checkup_GUI.py<br>
