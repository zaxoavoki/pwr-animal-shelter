import { Container, Row, Image, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import styles_main from "./AnimalInfoClient.module.css";
import styles_photo from "../../AnimalPhotoContainer.module.css";
import styles_button from "../../../../components/shared/Button.module.css";
import { Animal } from "../../../../types/Animal";
import { useParams } from "react-router";
import { useQuery } from "react-query";
import { fetchAnimal } from "../../../../api/animals";
import { useHistory } from 'react-router-dom';

export default function AnimalInfoClient() {
  const animalPhotos = [
    "https://thumbs.dreamstime.com/b/dog-golden-retriever-jumping-autumn-leaves-autumnal-sunlight-77861618.jpg",
    "https://thumbs.dreamstime.com/b/retriever-%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B8-%D0%B7%D0%BE%D0%BB%D0%BE%D1%82%D0%B8%D1%81%D1%82%D1%8B%D0%B9-21668976.jpg",
    "https://thumbs.dreamstime.com/b/retriever-%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B8-%D0%B7%D0%BE%D0%BB%D0%BE%D1%82%D0%B8%D1%81%D1%82%D1%8B%D0%B9-683752.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFv4rsjjJZd23tvUTxzzBQRi-XGDf8_n1vJvP1RMN0_6Q2CgHY_UY5lQh87NwHRXp10F8&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGMvZFqb35VZYb6ZyuSDs37F6L9gduGexaFEai_cbY2f7R-IiCR2dBzWmEKRIE-Yh0Olo&usqp=CAU",
  ];

  let history = useHistory();
  const redirect = () => {
    history.push("/animal-reservation/"+id)
  }

  const { id } = useParams<{ id: string }>();
  const { isLoading, isError, data } = useQuery<Animal>("fetchAnimal", () =>
    fetchAnimal(id)
  );

  if (isLoading) {
    return <>Loading</>;
  }

  if (isError) {
    return <>Error</>;
  }

  if (!data) {
    return <>Something went wrong</>;
  }

  return (
    <>
      <Container fluid className={styles_main["top-header"]} />
      <Container fluid className={styles_main["header-animal-info"]}>
        <Image
          src="https://ieltsninja.com/content/wp-content/uploads/2021/01/Describe-an-Interesting-Animal-Dog.jpg"
          className={styles_main["animal-photo"]}
          alt={"animal photo"}
        />
        <p className={styles_main["text-header"]}>
          <p>
            <b>{data.name}</b>
          </p>
          <hr />
          <p>{data.age} lat</p>
        </p>
      </Container>

      <Container className={styles_main["main-container"]}>
        <Row className={styles_main["animal-description"]}>
          {data.description}
        </Row>

        <Container className={styles_main["main-info-container"]}>
          <Container className={styles_main["info-decoration-container"]}>
            <span />
            <hr />
          </Container>

          <Container className={styles_main["info"]}>
            <p>
              <b>Status: </b>
              {data.animal_status.value}
            </p>
            <p>
              <b>Rasa: </b>
              {data.animal_breed.value}
            </p>
            <p>
              <b>P??e??: </b>
              {data.animal_gender.value}
            </p>
            <p>
              <b>Wzrost: </b>
              {data.height} cm
            </p>
          </Container>
        </Container>

        <Container className={styles_photo["photo-container"]}>
          {animalPhotos.map((photo) => (
            <Image
              className={styles_photo["photo"]}
              src={photo}
              alt="animal photo"
              onClick={() => window.open(photo)}
            />
          ))}
        </Container>
      </Container>

      <Container className={styles_main["nav-area"]}>
        <Link to={"/animal-reservation/"+id} className={styles_main["link"]}>
          <Button className={styles_button["button-green"]} onClick={redirect}>Zarezerwuj</Button>
        </Link>
      </Container>
    </>
  );
}
