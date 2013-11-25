import alvi.client.api
import alvi.client.api.array as array
import alvi.client.containers


class ArrayCreateElement(alvi.client.api.BaseScene):
    def run(self, pipe):
        n = 4
        for i in range(n):
            array.create_element(pipe, id=i, value=i)
        pipe.sync()

    @classmethod
    def container_name(cls):
        return "Array"


if __name__ == "__main__":
    ArrayCreateElement.start()