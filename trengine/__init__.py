from . import ajax, google, hozory, tdict

__all__ = ["AsyncEngine", "Engine"]


class Engine:
    def __init__(self) -> None:
        pass

    @property
    def ajax(self) -> "ajax.AjaxTranslator":
        return ajax.AjaxTranslator()

    @property
    def google(self) -> "google.GoogleTranslator":
        return google.GoogleTranslator()

    @property
    def hozory(self) -> "hozory.HozoryTranslator":
        return hozory.HozoryTranslator()

    @property
    def tdict(self) -> "tdict.TdictTranslator":
        return tdict.TdictTranslator()


class AsyncEngine:
    def __init__(self) -> None:
        pass

    @property
    def ajax(self) -> "ajax.AsyncAjaxTranslator":
        return ajax.AsyncAjaxTranslator()

    @property
    def google(self) -> "google.AsyncGoogleTranslator":
        return google.AsyncGoogleTranslator()

    @property
    def hozory(self) -> "hozory.AsyncHozoryTranslator":
        return hozory.AsyncHozoryTranslator()

    @property
    def tdict(self) -> "tdict.AsyncTdictTranslator":
        return tdict.AsyncTdictTranslator()
