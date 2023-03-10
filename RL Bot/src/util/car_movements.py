from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket
from sequence import Sequence, ControlStep

def begin_front_flip(packet=GameTickPacket):
    active_sequence = Sequence([
        ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
        ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
        ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, pitch=-1)),
        ControlStep(duration=0.8, controls=SimpleControllerState()),
    ])

    return active_sequence.tick(packet)

# Back flip code
def begin_back_flip(packet):
    active_sequence = Sequence([
    ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
    ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
    ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, pitch=1)),
    ControlStep(duration=0.8, controls=SimpleControllerState()),
    ])

    return active_sequence.tick(packet)

# Side flip left 
def begin_side_flip_left(self, packet = GameTickPacket):
        self.active_sequence = Sequence([
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, roll=-1)),
            ControlStep(duration=0.8, controls=SimpleControllerState()),
        ])

        return self.active_sequence.tick(packet)

# Side flip right 
def begin_side_flip_right(self, packet=GameTickPacket):
        self.active_sequence = Sequence([
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, roll=1)),
            ControlStep(duration=0.8, controls=SimpleControllerState()),
        ])

        return self.active_sequence.tick(packet)

# Diagonal flip forward right
def begin_diagonal_flip_forwards_right(self, packet=GameTickPacket):
        self.active_sequence = Sequence([
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, roll=1, pitch = -1)),
            ControlStep(duration=0.8, controls=SimpleControllerState()),
        ])

        return self.active_sequence.tick(packet)

# Diagonal flip forward left
def begin_diagonal_flip_forwards_left(self, packet=GameTickPacket):
        self.active_sequence = Sequence([
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, roll=-1, pitch = -1)),
            ControlStep(duration=0.8, controls=SimpleControllerState()),
        ])

        return self.active_sequence.tick(packet)

# Diagonal flip backwards right
def begin_diagonal_flip_backwards_right(self, packet=GameTickPacket):
        self.active_sequence = Sequence([
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, roll=1, pitch = 1)),
            ControlStep(duration=0.8, controls=SimpleControllerState()),
        ])

        return self.active_sequence.tick(packet)

# Diagonal flip backwards left
def begin_diagonal_flip_backwards_left(self, packet):
        self.active_sequence = Sequence([
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, roll=-1, pitch = 1)),
            ControlStep(duration=0.8, controls=SimpleControllerState()),
        ])

        return self.active_sequence.tick(packet)

def begin_halfflip(self, packet=GameTickPacket):
    self.active_sequence = Sequence([
        ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
        ControlStep(duration=0.05, controls=SimpleControllerState(jump=False)),
        ControlStep(duration=0.1, controls=SimpleControllerState(jump=True, pitch=1)), #backflip
        ControlStep(duration=0.2, controls=SimpleControllerState(jump=False, pitch=-1)), #cancel flip
        
        #Adjust duration so it lands well
        ControlStep(duration=0.2, controls=SimpleControllerState(jump=False, roll=1)), #airrollround
        ControlStep(duration=0.8, controls=SimpleControllerState()),

    ])
    return self.active_sequence.tick(packet)

    def begin_speed_flipwrong(self, packet):
        self.active_sequence = Sequence([
            ControlStep(duration=0.05, controls=SimpleControllerState(jump=True)),
            ControlStep(duration=0.001, controls=SimpleControllerState(jump=False)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=True, roll=-1, pitch = -1, boost=True)),
            ControlStep(duration=0.2, controls=SimpleControllerState(jump=False, roll=1, pitch = 1, boost=True ,handbrake=True)),

            ControlStep(duration=0.8, controls=SimpleControllerState()),
        ])

        # Return the controls associated with the beginning of the sequence so we can start right away.
        return self.active_sequence.tick(packet)