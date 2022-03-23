import av
import av.datasets
import numpy

from pprint import pprint


class FFmpeg:
    def __init__(self, file, mode, **kwargs):
        self.ffmpeg = av.open(av.datasets.curated(file), mode, **kwargs)
        self.streams = self.ffmpeg.streams

        print(self.streams.get())

        if mode == 'r':
            self.file_info = {
                'codec_name': self.ffmpeg.format.name,
                'codec_long_name': self.ffmpeg.format.long_name,
                'streams': {
                    'audio': [],
                    'video': [],
                    'subtitles': [],
                    'data': [],
                    'other': []
                }
            }

            self.loader = {
                'state': 'stop',

                'generator': None,
                'audio_processor': [self.convert_to_array],
                'video_processor': [self.convert_to_image],
                'frame_size': None
            }

            self._get_stream_options()

            pprint(self.file_info)
            pprint(self.loader)

    def load(self, audio=None, video=None):
        if audio is not None:
            pass

        elif video is not None:
            pass

    def _get_stream_options(self):
        for stream in self.streams.get():
            cc = stream.codec_context

            stream_options = {
                'duration': stream.duration,
                'id': stream.id,
                'index': stream.index,
                'lang': stream.language,
                'meta': stream.metadata,
                'frame_count': stream.frames,
                'bit_rate': cc.bit_rate,
                'codec_name': cc.name,
                'codec_long_name': cc.codec.long_name,
                'delay': cc.codec.delay,
                'time_base': stream.time_base,
                'start_time': stream.start_time
            }

            self.file_info['streams'][stream.type].append({k: v for k, v in stream_options.items()})

            if stream.type == 'video':
                stream_video_options = {
                    'height': cc.height,
                    'width': cc.width,
                    'fps': stream.base_rate,
                    'aspect_ratio': cc.sample_aspect_ratio
                }

                self.file_info['streams'][stream.type].append({k: v for k, v in stream_video_options.items()})

            elif stream.type == 'audio':
                stream_audio_options = {
                    'channels': cc.channels,
                    'channel_name': cc.layout.name,
                    'sample_rate': stream.sample_rate,
                    'frame_size': cc.frame_size
                }

                self.file_info['streams'][stream.type].append({k: v for k, v in stream_audio_options.items()})

    @staticmethod
    def convert_to_image(frame):
        try:
            return frame.to_image()
        except:
            return frame.to_rgb().to_image()

    @staticmethod
    def convert_to_array(frame):
        return numpy.transpose(frame.to_ndarray().copy(other='C'))


if __name__ == '__main__':
    FFmpeg(r'', 'r')