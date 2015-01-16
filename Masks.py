__author__ = 'Agnieszka'


class Masks(object):
    def __init__(self, prostata, bladder, rectum, femurR, feumrL, semi_vesicle,sum=0):
        '''
        Binary masks 0 in no organ 1 is organ
        :param prostata:
        :param bladder:
        :param rectum:
        :param femurR:
        :param feumrL:
        :param semi_vesicle:
        :return:
        '''
        self.prostate = prostata
        self.bladder = bladder
        self.rectum = rectum
        self.femurR = femurR
        self.femurL = feumrL
        self.semi_vesicle = semi_vesicle
        self.sum_mask = self.prostate + self.bladder + self.rectum + self.femurL + self.femurR + self.semi_vesicle


class keyPoints_in_organ(object):
    def __init__(self, prostata_keypoints, bladder_keypoints, rectum_keypoints, femurR_keypoints, feumrL_keypoints,
                 semi_vesicle_keypoints):
        '''
        keypoints with keypoint descriptor, orientation and localization as a vector
        :param prostata_keypoints:
        :param bladder_keypoints:
        :param rectum_keypoints:
        :param femurR_keypoints:
        :param feumrL_keypoints:
        :param semi_vesicle_keypoints:
        :return:
        '''

        self.prostate_keypoints = prostata_keypoints
        self.bladder_keypoints = bladder_keypoints
        self.rectum_keypoints = rectum_keypoints
        self.femurR_keypoints = femurR_keypoints
        self.femurL_keypoints = feumrL_keypoints
        self.semi_vesicle_keypoints = semi_vesicle_keypoints