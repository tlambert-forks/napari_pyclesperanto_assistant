import pytest
# import napari_pyclesperanto_assistant

def test_whatever2(make_napari_viewer):
    viewer = make_napari_viewer()


# @pytest.mark.skip
# def test_whatever3(make_napari_viewer):
#     viewer = make_napari_viewer()
#     assistant_gui = napari_pyclesperanto_assistant.napari_plugin(viewer)


# @pytest.mark.skip
# def test_complex_workflow():
#     print("x")

#     import napari
#     import napari_pyclesperanto_assistant
#     from pathlib import Path

#     print("7")

#     root = Path(napari_pyclesperanto_assistant.__file__).parent

#     filename = str(root / "data" / "Lund_000500_resampled-cropped.tif")
#     # filename = str(root / 'data' / 'CalibZAPWfixed_000154_max-16.tif')

#     # create Qt GUI context
#     print("a")
#     napari.gui_qt()

#     # start napari
#     print("b")
#     viewer = napari.Viewer(show=False)

#     print("c")
#     layer = viewer.open(filename)
#     layer[0].metadata["filename"] = filename

#     # attach the assistant
#     print("d")
#     assistant_gui = napari_pyclesperanto_assistant.napari_plugin(viewer)

#     print("e")
#     from .._operations._operations import (
#         denoise,
#         background_removal,
#         filter,
#         binarize,
#         combine,
#         label,
#         label_processing,
#         map,
#         mesh,
#         measure,
#         label_measurements,
#         transform,
#         projection,
#     )

#     assistant_gui._activate(denoise)
#     print("f")
#     assistant_gui._activate(background_removal)
#     assistant_gui._activate(filter)
#     assistant_gui._activate(binarize)

#     print("g")
#     viewer.close()
