import { JSX } from 'react';
import PageLayout from '@/components/PageLayout/PageLayout';

const SettingsPage = (): JSX.Element => {
  return (
    <PageLayout>
      <h1>Settings page</h1>
      <ul>
        <li>setting 1</li>
        <li>setting 2</li>
        <li>setting 3</li>
        <li>setting 4</li>
        <li>setting 5</li>
      </ul>
    </PageLayout>
  );
};
export default SettingsPage;
