import { useState } from 'react';
import axios from 'axios';
import { FormikProvider, useFormik } from "formik";
import Button from 'react-bootstrap/Button';
import Table from 'react-bootstrap/Table';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Container from "react-bootstrap/esm/Container";

import IndexNavbar from "./Navbar.jsx";
import routes from '../routes/routes.js';


const IndexPage = () => {
  const [files, setFiles] = useState([]);

  let count = 0;

  const handleSubmit = async (values) => {
    const requestBody = {
      'link': values.link
    }
    try {
      const response = await axios.post(routes.linksPath, requestBody)
      setFiles(response.data)

    } catch (e) {
      console.log('error', e);
    }
  };

  const downloadHandler = async (file) => {
    const response = await axios.get(file.link, { responseType: 'blob' })
    const url = URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", file.filename);
    link.click();
  }

  const formik = useFormik({
    initialValues: {
      link: '',
    },
    onSubmit: (values) => handleSubmit(values),
  });

  return <>
  <IndexNavbar/>
  <FormikProvider value={formik}>
  <h2 className="text-center mb-4">Введите публичную ссылку на Яндекс диск</h2>
    <Form onSubmit={formik.handleSubmit} className="justify-content-md-center">
      <Container className="mb-3">
      <Row>
        <Col>
        <Form.Group className="form-floating mb-3">
        <Form.Control
          id="link"
          onChange={formik.handleChange}
          value={formik.values.link}
        />
        <Form.Label htmlFor='link' >Ссылка</Form.Label>
        </Form.Group>
        </Col>
      </Row>
      <Button type="submit">
        Отправить
      </Button>
      </Container>
      {files.length > 0 &&
      <Container>
      <Table striped bordered hover className="text-center">
          <thead>
            <tr>
              <th>Номер файла</th>
              <th>Название</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
          {files.map((file) => {
          count += 1;
          return <tr key={count}>
            <td>{count}</td>
            <td>{file.filename}</td>
            <td><button type="button" onClick={() => downloadHandler(file)}>Скачать</button></td>
          </tr>
          // return <Row key={count}>{count}: <a href={file.link}>{file.filename}</a></Row>
        })}

          </tbody>
        </Table> 

      </Container>
      }

    </Form>
  </FormikProvider>

  </>

}

export default IndexPage;