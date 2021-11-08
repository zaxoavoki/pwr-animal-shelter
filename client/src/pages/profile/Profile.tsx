import { useContext } from "react";
import { Container, Image, Button } from "react-bootstrap";
import { useQuery } from "react-query";
import { Link, useParams } from "react-router-dom";
import { fetchProfileData } from "../../api/profile";
import { AuthContext } from "../../contexts/AuthContext";
import styles from "./Profile.module.css";

const FIELDS_TO_SHOW = [
  ["first_name", "Imię"],
  ["last_name", "Nazwisko"],
  ["pesel", "PESEL"],
  ["address", "Adres"],
  ["phone", "Tel."],
  ["email", "E-mail"],
];

export default function Profile() {
  const { id } = useParams<{ id: string }>();
  const { auth } = useContext(AuthContext);
  const { isLoading, isError, data } = useQuery(
    ["getProfileData", id],
    () => fetchProfileData(id),
    { retry: false }
  );

  if (isLoading) {
    return <>Loading</>;
  }

  if (isError) {
    return <h1>Error has occured</h1>;
  }

  return (
    <>
      <Container fluid className={styles["top-page"]} />
      <div className="mx-auto text-center">
        <Image
          roundedCircle
          className={styles["top-page__header__user-img"]}
          src="https://ath2.unileverservices.com/wp-content/uploads/sites/4/2020/02/IG-annvmariv-1024x1016.jpg"
          alt="User's image"
        />
        <h1 className={styles["top-page__header__title"]}>Moje dane</h1>
      </div>
      <Container className={styles["user-info"]}>
        {FIELDS_TO_SHOW.map(
          ([key, text]) =>
            data[key] && (
              <p key={key}>
                {text}: <span>{data[key]}</span>
              </p>
            )
        )}
      </Container>
      {auth.user && (
        <Link to="/profile/2" className="text-decoration-none">
          <Button className={styles["btn-modify"]}>Modyfikuj</Button>
        </Link>
      )}
    </>
  );
}
