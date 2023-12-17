import { JSX } from 'react';
import { Link } from 'react-router-dom';
import PageLayout from '@/components/PageLayout/PageLayout';

const NotFoundPage = (): JSX.Element => {
  return (
    <PageLayout>
      <h1>Not Found...</h1>
      <Link to={'/'}>Back to main</Link>
    </PageLayout>
  );
};
export default NotFoundPage;
