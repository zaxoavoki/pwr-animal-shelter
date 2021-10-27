import { Link } from "react-router-dom";
import styles from "./SubMenu.module.css";

export type MenuLink = {
  path: string;
  text: string;
  submenu?: MenuLink[];
};

export default function SubMenu({
  isOpened,
  links,
}: {
  isOpened: boolean;
  links?: MenuLink[];
}) {
  return (
    <ul
      className={
        styles["c-header__menu__submenu"] + (!isOpened ? " d-none" : " d-block")
      }
    >
      {links && links.map(({ path, text }, i) => (
        <li key={i}>
          <Link to={path}>{text}</Link>
        </li>
      ))}
    </ul>
  );
}
