import play
import skills.move
import behavior
import robocup
import math


class TeeUp(play.Play):
    def __init__(self):
        super().__init__(continuous = False)

        self.add_transition(behavior.Behavior.State.start,
            behavior.Behavior.State.running,
            lambda: True,
            'immediately')
        self.add_transition(behavior.Behavior.State.running,
            behavior.Behavior.State.completed,
            lambda: self.subbehavior_with_name("robot0").state == behavior.Behavior.State.completed,
            'all robots reach target positions')
        self.add_transition(behavior.Behavior.State.completed,
            behavior.Behavior.State.running,
            lambda: self.subbehavior_with_name("robot0").state == behavior.Behavior.State.running,
            'robots arent teed up')

        # step = 1
        # for i in range(4):
        #     pt = robocup.Point(0, 2 + i * step)
        #     self.add_subbehavior(skills.move.Move(pt),
        #         name="robot" + str(i),
        #         required=False,
        #         priority=6 - i)
        # self.add_subbehavior(skills.move.Move(robocup.Point(-step, 2 + 3 * step)),
        #         name="robot" + str(4),
        #         required=False,
        #         priority=6 - i)
        # self.add_subbehavior(skills.move.Move(robocup.Point(step, 2 + 3 * step)),
        #         name="robot" + str(5),
        #         required=False,
        #         priority=6 - i)

        h = 0
        k = 4
        r = 1
        offset = 0
 
        self.remove_all_subbehaviors()
        for i in range(6):
            pt = robocup.Point(h + r * math.cos(math.pi / 3 * i + offset), k + r * math.sin(math.pi / 3 * i + offset))
            self.add_subbehavior(skills.move.Move(pt),
                name="robot" + str(i),
                required=False,
                priority=6 - i)
        


