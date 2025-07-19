from nanobind_viser_repro import DummyClass

from viser import ViserServer

class Example:
    def __init__(self):
        # Create a Viser server with a transform control gizmo.
        server = ViserServer()
        controls = server.scene.add_transform_controls(
            "/marker/",
            depth_test=False,
            scale=0.2,
            disable_sliders=True,
            visible=True,
        )

        # Create a nanobind binded object to demonstrate reference leaking.
        self.dc = DummyClass()

        # Set an update callback to the gizmo -- this is what demonstrates the leakage!
        controls.on_update(self.say_hello)

    def say_hello(self, _):
        print(self.dc)

if __name__ == "__main__":
    ex = Example()
