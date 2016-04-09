import org.eclipse.jface.viewers.TableViewer;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Table;
import org.eclipse.tracecompass.analysis.timing.ui.views.segmentstore.density.AbstractSegmentStoreDensityView;
import org.eclipse.tracecompass.analysis.timing.ui.views.segmentstore.density.AbstractSegmentStoreDensityViewer;
import org.eclipse.tracecompass.analysis.timing.ui.views.segmentstore.table.AbstractSegmentStoreTableViewer;
import org.eclipse.tracecompass.internal.analysis.os.linux.ui.views.latency.SystemCallLatencyTableViewer;

/**
 * System Call Density view
 *
 * @author Matthew Khouzam
 * @author Marc-Andre Laperle
 */
public class FrankSegmentView extends AbstractSegmentStoreDensityView {

    /** The view's ID */
    public static final String ID = "org.eclipse.tracecompass.internal.lttng2.kernel.ui.frankSegmentView.view"; //$NON-NLS-1$

    /**
     * Constructs a new density view.
     */
    public FrankSegmentView() {
        super(ID);
    }

    @SuppressWarnings("restriction")
    @Override
    protected AbstractSegmentStoreTableViewer createSegmentStoreTableViewer(Composite parent)
    {
        return new SystemCallLatencyTableViewer(new TableViewer(parent, SWT.FULL_SELECTION | SWT.VIRTUAL)) {
            @Override
            protected void createProviderColumns() {
                super.createProviderColumns();
                Table t = (Table) getControl();
                t.setColumnOrder(new int[] { 3, 2, 0, 1 });
            }
        };
    }

    @Override
    protected AbstractSegmentStoreDensityViewer createSegmentStoreDensityViewer(Composite parent) {
        return new FrankDensityViewer(parent);
    }

}
