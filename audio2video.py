import argparse

from moviepy import AudioFileClip, ImageClip

def audio_to_video_with_cover(input_path, cover_path, output_path, fps):
    with AudioFileClip(input_path) as audio_clip, ImageClip(cover_path) as cover_clip:
        cover_clip = cover_clip.with_duration(audio_clip.duration).with_audio(audio_clip)
        cover_clip.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            fps=fps,
            bitrate="1000k",
        )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input.mp3')
    parser.add_argument('--cover', default='cover.png')
    parser.add_argument('--output', default='output.mp4')
    parser.add_argument('--fps', default=1)
    args = parser.parse_args()

    try:
        audio_to_video_with_cover(args.input, args.cover, args.output, args.fps)
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()