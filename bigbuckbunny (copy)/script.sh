ffmpeg -i Shingeki_no_Kyojin_S2_-_11.mkv -c:v copy -c:a aac -map 0 -scodec webvtt \
  -map 0 -scodec webvtt -map 0 -scodec webvtt -f hls -hls_time 10 -hls_list_size 0 \
  -hls_segment_filename 'segment%d.ts' -var_stream_map "a:0,sgroup:audio0 a:1,sgroup:audio1 a:2,sgroup:audio2 s:0,sgroup:subtitle0 s:1,sgroup:subtitle1 s:2,sgroup:subtitle2" \
  -master_pl_name master.m3u8 output_%v.m3u8
