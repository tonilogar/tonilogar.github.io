// Sustituye los valores siguientes por tu URL de proyecto y clave anónima
// desde el panel de Supabase (Settings > API).
const SUPABASE_URL = 'https://askupkcqzqephgdsvabc.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFza3Vwa2NxenFlcGhnZHN2YWJjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE1ODQ1NzUsImV4cCI6MjA3NzE2MDU3NX0.HLnq66pm7tAm-2cSDikEuLvZ1JQlbhAIJgTJpgr4Pq4';

if (!window.supabase) {
    console.error("Supabase JS SDK no está disponible. Revisa el script CDN.");
}

const supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
