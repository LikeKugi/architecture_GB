import { FC, JSX, PropsWithChildren } from 'react';
import styles from './PageLayout.module.scss';

const PageLayout: FC<PropsWithChildren> = ({ children }): JSX.Element => {
  return (
    <div className={styles.PageLayout}>
      {children}
    </div>
  );
};
export default PageLayout;
