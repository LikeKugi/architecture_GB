export const enum RoutesConstants {
  INDEX = '/',
  NOT_FOUND = '*',
  SETTINGS = '/settings',
  ABOUT = '/about',
}

export const RoutesMapping = {
  [RoutesConstants.INDEX]: 'Main',
  [RoutesConstants.ABOUT]: 'About',
  [RoutesConstants.SETTINGS]: 'Settings',
};
