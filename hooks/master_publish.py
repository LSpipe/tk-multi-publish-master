#    Hook for changing the versions for master publish.

import os
import maya.cmds as cmds

import tank
from tank import Hook
from tank import TankError

class MasterPublishHook(Hook):
    def execute(self, task, work_template):
        # get scene path
        scene_path = os.path.abspath(cmds.file(query=True, sn=True))
        fields = work_template.get_fields(scene_path)
        print fields
#         fields['Step'] = 'Master'
#         print work_masater_template.apply_fields(fields)
        return task
        