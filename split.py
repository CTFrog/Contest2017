from pathlib import Path
from PIL import Image, ImageSequence

# 分割したいアニメーション GIF 画像
IMAGE_PATH = '02_anime2.gif'
# 分割した画像の出力先ディレクトリ
DESTINATION = 'splitted'
# 現在の状況を標準出力に表示するかどうか
DEBUG_MODE = True


def main():
    frames = get_frames(IMAGE_PATH)
    write_frames(frames, IMAGE_PATH, DESTINATION)


def get_frames(path):
    '''パスで指定されたファイルのフレーム一覧を取得する
    '''
    im = Image.open(path)
    return (frame.copy() for frame in ImageSequence.Iterator(im))


def write_frames(frames, name_original, destination):
    '''フレームを別個の画像ファイルとして保存する
    '''
    path = Path(name_original)

    stem = path.stem
    extension = path.suffix

    # 出力先のディレクトリが存在しなければ作成しておく
    dir_dest = Path(destination)
    if not dir_dest.is_dir():
        dir_dest.mkdir(0o700)
        if DEBUG_MODE:
            print('Destionation directory is created: "{}".'.format(destination))

    for i, f in enumerate(frames):
        name = '{}/{}-{}{}'.format(destination, stem, i + 1, extension)
        f.save(name)
        if DEBUG_MODE:
            print('A frame is saved as "{}".'.format(name))


if __name__ == '__main__':
    main()

