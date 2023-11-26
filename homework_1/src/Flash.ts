class Flash {
  constructor(public location: IPoint, public angle: Angle, public color: IColor, public power: number) {
  }

  rotate(angle: Angle) {
    this.angle = angle;
  }

  move(location: IPoint) {
    this.location = location;
  }
}
