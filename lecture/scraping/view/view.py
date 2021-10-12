from lecture.common import Dataset
from lecture.common import Service

class View (object):
    dataset = Dataset()
    service = Service()

    def modeling(self, bugs, melon):
        modeling = self.proprcessing(bugs, melon)
        print(type(modeling.context))
        print(modeling.context.head(2))
        print(modeling.fname.head(2))

    def proprcessing(self, bugs, melon):
        this = self.dataset
        service = self.service
        this.context = service.new_model(bugs)
        this.fname = service.new_model(melon)
        return this


