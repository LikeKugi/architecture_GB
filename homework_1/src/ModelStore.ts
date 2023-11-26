class ModelStore {
  models: PolygonalModel[];
  scenes: Scene[];
  flashes: Flash[];
  cameras: Camera[];
  getScene(sceneId: number) {
    return this.scenes.filter(scene => scene.id)
  }
  notifyChange() {

  }
}
