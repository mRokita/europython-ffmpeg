import ffmpeg

stream = ffmpeg.input("viofo_ph.mp4").filter("scale", w=300, h=300, force_original_aspect_ratio=1).filter_multi_output("split", 1)
padded = stream[0].filter("pad", w=300, h=300, x="(ow-iw)/2", y=("(oh-ih)/2"))

cmd = ffmpeg.merge_outputs(stream[1].output("1.mp4"), padded.output("2.mp4"))
print(cmd.compile())
cmd.run()