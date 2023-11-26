interface IPoint {
  x: number;
  y: number;
  z: number;
}

interface ITexture {
  id: number;
  getId: () => number;
  name: string;
  getName: () => string;
}

type TPolygon = IPoint[]

interface IColor {
  red: number;
  green: number;
  blue: number;
}
