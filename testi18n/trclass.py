import gettext
import os

class TrClass():
    def __init__(self):
        self._val = 42
        self._init_lang()

    def myprint(self):
        print(self._val)
        # FIXME --- non sono riuscito a capire come fare in questo
        # contesto ad utilizzare "_"
        print(self._t.gettext('inside translatable class'))

    def setlang(self, lang):
        # FIXME --- cosi' funziona, ma non sono riusciuto a capire se esiste
        # un sistema piu' semplice per cambiare il linguaggio senza costringere
        # il programma che usa questa classe a chiamare questa setlang()
        # tutte le volte che la main application cambia il linguaggio.
        self._t = lang
        _ = self._t.gettext

    # ------------------------------------------------------------------------
    def _init_lang(self):
        # set default language to the system one. For example is the system
        # variable LANGUAGE is set to 'en_US' the translations are searched in
        # the <localdir>/locale/en_US/ directory. If not found does not translate
        ldir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        self._t = gettext.translation('messages', ldir, fallback=True)
        _ = self._t.gettext

