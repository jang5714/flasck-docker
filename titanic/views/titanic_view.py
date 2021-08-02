from titanic.models.dataset import Dataset
from titanic.models.service import TitanicService


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        this = self.service
        return this

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        return this