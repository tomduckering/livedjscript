import logging
import Live

logger = logging.getLogger('AAATOMD')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/tmp/AAATOMD.ableton.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

#logger.info(dir())

class AAATOMD():
    """ Custom stuffs """

    def __init__(self, c_instance):
        logger.info('In the init for AAATOMD')
        c_instance.log_message("adsfadfasdfasdfd")
        self.c_instance = c_instance
        
        things = dir(self.c_instance)
        #logger.info(things)
        self.c_instance.show_message("Tom D calling!!!")
        handle = self.c_instance.handle()
        #logger.info(type(self.c_instance))
        #logger.info(dir())
        #logger.info(dir(Live))
        application = Live.Application.get_application()
        #logger.info(dir(application))
        #logger.info(dir(Live.Song.Song))
        current_song = application.get_document()
        logger.info(type(current_song))
        logger.info(dir(current_song))
        
        
