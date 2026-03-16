class Cone:
    @staticmethod
    def areaofCone(r, h):
        return 3.14 * r * r * h / 3
    
class Cylinder:
    @staticmethod
    def areaofCylinder(r, h):
        return 2 * 3.14 * r * (r + h)

h = float(input("Enter height: "))
r = float(input("Enter radius: "))

print("Cone area:", Cone.areaofCone(r, h))
print("Cylinder area:", Cylinder.areaofCylinder(r, h))
