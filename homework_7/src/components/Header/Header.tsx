import { JSX } from 'react';
import { RoutesMapping } from '@/constants';
import { NavLink } from 'react-router-dom';
import styles from './Header.module.scss';

const Header = (): JSX.Element => {
  return (
    <header className={styles.header}>
      <nav className={styles.header__nav}>
        {Object.entries(RoutesMapping).map(([path, title]) => (<NavLink className={styles.header__link}
                                                                        to={path}>{title}</NavLink>))}
      </nav>
    </header>
  );
};
export default Header;
