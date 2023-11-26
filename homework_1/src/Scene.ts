class Scene {
  static ID = 0;
  models: PolygonalModel[] = [];
  flashes: Flash[]
  id: number;
  constructor() {
    Scene.ID += 1;
    this.id = Scene.ID
  }

  addPolygonalModel(model: PolygonalModel) {
    this.models.push(model);
  }
  addFlash(flash: Flash) {
    this.flashes.push(flash);
  }
}
