import { JSX } from 'react';
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom';
import { RoutesConstants } from '@/constants';
import RootPage from '@/pages/RootPage/RootPage';
import MainPage from '@/pages/MainPage/MainPage';
import AboutPage from '@/pages/AboutPage/AboutPage';
import NotFoundPage from '@/pages/NotFoundPage/NotFoundPage';
import SettingsPage from '@/pages/SettingsPage/SettingsPage';

const routes = createBrowserRouter(createRoutesFromElements(
  <Route path={RoutesConstants.INDEX}
         element={<RootPage/>}>
    <Route index
           element={<MainPage/>}/>
    <Route path={RoutesConstants.ABOUT}
           element={<AboutPage/>}/>
    <Route path={RoutesConstants.SETTINGS}
           element={<SettingsPage/>}/>
    <Route path={RoutesConstants.NOT_FOUND}
           element={<NotFoundPage/>}/>
  </Route>
));

const AppRouter = (): JSX.Element => {
  return (
    <RouterProvider router={routes}/>
  );
};
export default AppRouter;
