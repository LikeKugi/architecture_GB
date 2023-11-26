class Camera {
  constructor(public location: IPoint, public angle: Angle) {
  }

  rotate(angle: Angle) {
    this.angle = angle;
  }

  move(location: IPoint) {
    this.location = location;
  }
}
