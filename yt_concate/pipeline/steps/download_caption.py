import time

from pytube import YouTube

from .step import Step, StepException


class DonwloadCaption(Step):
    start = time.time()
    def process(self, data, inputs, utils):
        print('downloading caption for: ', url)
        for url in data:
            if utils.caption_file_exists(url):
                print('found existing caption files')
                continue
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_str = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for: ', url)
                continue

            # find out video id from url and save caption to id.txt
            text_file = open(utils.get_caption_filepath(url), 'w', encoding='utf-8')
            text_file.write(en_caption_convert_to_str)
            text_file.close()
            break
        end = time.time()
        print('time took:', end - start, 'secs')







