from nanobind_viser_repro import DummyClass

from viser import ViserServer

def main():
    # Create a Viser server with a transform control gizmo.
    server = ViserServer()
    controls = server.scene.add_transform_controls(
        "/ik_marker/",
        depth_test=False,
        scale=0.2,
        disable_sliders=True,
        visible=True,
    )

    # Create a nanobind binded object to demonstrate reference leaking.
    dc = DummyClass()

    # Set an update callback to the gizmo -- this is what demonstrates the leakage!
    @controls.on_update
    def say_hello(_):
        print(dc)

if __name__ == "__main__":
    main()