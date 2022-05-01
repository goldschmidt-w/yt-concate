

from pytube import YouTube

from .step import Step, StepException


class DonwloadCaption(Step):
    def process(self, data, inputs, utils):
        for url in data:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_str = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_str)
            # find out video id from url and save caption to id.txt
            text_file = open(utils.get_caption_path(url), 'w')
            text_file.write(en_caption_convert_to_str)
            text_file.close()
            break







