import xarm

arm = xarm.Controller('USB')

def placer(id, position):
    arm.setPosition(id, position, 500, True)

BRAS_HAUT     =  [ (3,500), (4,500), (5,500), (6,500)]
BRAS_BAS      =  [ (3,750), (4,250), (5,625), (6,500)]
MAIN_OUVERTE = [(1,0)]
MAIN_FERMEE  = [(1,999)]
POIGNET_DROIT = [(2,500)]
POIGNET_ANGLE = [(2,999)]

positions = [ BRAS_HAUT,
              POIGNET_DROIT,
              MAIN_OUVERTE,
              MAIN_FERMEE,
              MAIN_OUVERTE,
              POIGNET_DROIT,
              POIGNET_ANGLE,
              POIGNET_DROIT,
              BRAS_BAS,
              MAIN_FERMEE,
              POIGNET_DROIT,
              POIGNET_ANGLE,
              POIGNET_DROIT,
              BRAS_HAUT,
             ]


for position in positions:
    for id, p in position:
        placer(id, p)
