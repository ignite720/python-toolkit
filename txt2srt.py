from datetime import timedelta

import pysubs2

def timedelta_to_milliseconds(td: timedelta):
    return td.total_seconds() * 1000

def txt_to_srt(
    input_file: str,
    output_file: str,
    chars_per_sec: float = 3.9,
    line_interval: float = 1.0,
):
    with open(input_file, mode="r", encoding="utf-8") as fp:
        lines = [line.strip() for line in fp if line.strip()]

    subs = pysubs2.SSAFile()
    start_time = timedelta(seconds=0.0)
    for i, text in enumerate(lines):
        line_duration = max(1.0, len(text) / chars_per_sec)
        end_time = (start_time + timedelta(seconds=line_duration))

        subtitle_event = pysubs2.SSAEvent(
            start=timedelta_to_milliseconds(start_time),
            end=timedelta_to_milliseconds(end_time),
            text=text,
        )
        subs.append(subtitle_event)

        start_time = (end_time + timedelta(seconds=line_interval))
    subs.save(output_file)

txt_to_srt("input.txt", "output.srt")
