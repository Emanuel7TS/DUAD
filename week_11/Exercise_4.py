class Head:
    def __init__(self, hair_color):
        self.hair_color = hair_color

class Torso:
    def __init__(self, body_type):
        self.body_type = body_type

class Arm:
    def __init__(self, bicep_size):
        self.bicep_size = bicep_size        

class Hand:
    def __init__(self, psi):
        self.psi = psi

class Leg:
    def __init__(self, quadricep_size):
        self.quadricep_size = quadricep_size

class Feet:
    def __init__(self, shoe_size):
        self.shoe_size = shoe_size         

class Human:
    def __init__(self, head, torso, arm, hand, leg, feet):
        self.head = head
        self.torso = torso
        self.arm = arm
        self.hand = hand
        self.leg = leg
        self.feet = feet


head_hair_color = Head("Black hair")
torso_body_type = Torso("Body builder")
arm_bicep_size = Arm("60cm")
hand_psi = Hand("35 PSI")
leg_quadricep_size = Leg("95 cm")
feet_shoe_size = Feet("42")

human_full_body = Human(head_hair_color, torso_body_type, arm_bicep_size, hand_psi, leg_quadricep_size, feet_shoe_size)


print(f"The human has {human_full_body.head.hair_color} hair, "
      f"{human_full_body.torso.body_type} torso, "
      f"{human_full_body.arm.bicep_size} biceps, "
      f"{human_full_body.hand.psi} in PSI pressure, "
      f"{human_full_body.leg.quadricep_size} quadriceps, "
      f"and feet size {human_full_body.feet.shoe_size}.")
