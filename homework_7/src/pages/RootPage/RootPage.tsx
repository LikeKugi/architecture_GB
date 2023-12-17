import { JSX } from 'react';
import Header from '@/components/Header/Header';
import { Outlet } from 'react-router-dom';
import styles from './RootPage.module.scss';

const RootPage = (): JSX.Element => {
  return (
    <div className={styles.root}>
      <Header/>
      <div className={styles.root__content}>
        <Outlet/>
      </div>
    </div>
  );
};
export default RootPage;
