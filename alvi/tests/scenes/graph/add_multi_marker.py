from . import create_node
import alvi.client.api.common as common


class GraphAddMultiMarker(create_node.GraphCreateNode):
    def run(self, pipe):
        super().run(pipe)
        MULTI_MARKER_ID = 100
        common.create_multi_marker(pipe, MULTI_MARKER_ID, "multi marker")
        common.multi_marker_add_item(pipe, MULTI_MARKER_ID, 1)
        common.multi_marker_add_item(pipe, MULTI_MARKER_ID, 2)
        pipe.sync()