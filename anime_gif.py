from PIL import Image

# オリジナルのアニメーションgifを読み込む
im = Image.open('afterimage.gif')

# 結果書き込み用の164x164画像を作る
res = Image.new('RGB', (164, 164))

# 二次元配列の構造をしているpixクラスのインスタンスを返却する
pix = res.load()

# 二次元配列を白で埋めつくす
for y in range(164):
  for x in range(164):
    pix[x, y] = (255, 255, 255)

try:
  # フレーム分ループ
  while True:
    print(im.tell())
    # フレームのRGB二次元配列を取得
    im2 = im.convert('RGB').load()
    # 縦横164ピクセル全て処理
    for y in range(164):
      for x in range(164):
        # 黒じゃなかったら黒で塗る
        if im2[x, y] != (0, 0, 0):
          pix[x, y] = (0, 0, 0)
    # フレームを移動する
    im.seek(im.tell() + 1)

# フレームが終わりだったら終わり
except EOFError:
  pass

# 結果pngファイル書き込み
res.save('result.png')

